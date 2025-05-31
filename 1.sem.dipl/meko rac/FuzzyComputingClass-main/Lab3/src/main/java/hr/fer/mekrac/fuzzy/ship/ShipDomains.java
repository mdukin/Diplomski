package hr.fer.mekrac.fuzzy.ship;

import hr.fer.mekrac.fuzzy.domain.IDomain;
import hr.fer.mekrac.fuzzy.domain.SimpleDomain;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public class ShipDomains {
    private ShipDomains() {
    }

    public static final IDomain ANGLE = new SimpleDomain(- 90, 90 + 1);
    public static final IDomain DISTANCE = new SimpleDomain(0, 1300 + 1);
    public static final IDomain SPEED = new SimpleDomain(0, 100 + 1);
    public static final IDomain ACCELERATION = new SimpleDomain(- 50, 50 + 1);
    public static final IDomain RIGHT_PATH = new SimpleDomain(0, 1 + 1);
}
