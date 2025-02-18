import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
