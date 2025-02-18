import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BuyingPressure': 1.0
        })
    )
