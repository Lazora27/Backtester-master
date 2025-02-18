import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
