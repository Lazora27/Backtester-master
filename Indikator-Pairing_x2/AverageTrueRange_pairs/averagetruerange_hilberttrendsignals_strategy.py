import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
