import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
