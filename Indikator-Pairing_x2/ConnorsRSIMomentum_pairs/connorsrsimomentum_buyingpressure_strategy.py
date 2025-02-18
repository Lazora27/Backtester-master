import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSIMomentum_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSIMomentum und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ConnorsRSIMomentum': 1.0,
            'BuyingPressure': 1.0
        })
    )
