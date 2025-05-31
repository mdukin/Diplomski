package hr.fer.mekrac.fuzzy.domain;

/**
 * @author matejc
 * Created on 12.10.2022.
 */

public abstract class Domain implements IDomain {

    public static IDomain intRange(int start, int end) {
        return new SimpleDomain(start, end);
    }

    public static Domain combine(IDomain first, IDomain second) {
        SimpleDomain[] domains = new SimpleDomain[first.getNumberOfComponents() + second.getNumberOfComponents()];

        int counter = 0;
        for (int i = 0; i < first.getNumberOfComponents(); i++) {
            domains[counter++] = (SimpleDomain) first.getComponent(i);
        }
        for (int i = 0; i < second.getNumberOfComponents(); i++) {
            domains[counter++] = (SimpleDomain) second.getComponent(i);
        }

        return new CompositeDomain(domains);
    }


    @Override
    public int indexOfElement(DomainElement element) {
        var iterator = iterator();
        int counter = 0;
        while (iterator.hasNext()) {
            var el = iterator.next();
            if (el.equals(element)) return counter;
            counter++;
        }
        return - 1;
    }

    @Override
    public DomainElement elementForIndex(int index) {
        var iterator = iterator();
        int counter = 0;
        while (iterator.hasNext()) {
            var el = iterator.next();
            if (index == counter) {
                return el;
            }
            counter++;
        }
        return null;
    }
}
