import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ConnorsRSIMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ConnorsRSIMomentum
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ConnorsRSIMomentum': 1.0
        })
    )
