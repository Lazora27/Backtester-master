import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
