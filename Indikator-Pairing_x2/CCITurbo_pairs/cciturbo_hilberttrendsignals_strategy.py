import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
