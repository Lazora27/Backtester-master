import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'BuyingPressure': 1.0
        })
    )
