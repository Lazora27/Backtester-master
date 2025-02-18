import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedFractalEfficiency_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedFractalEfficiency und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PolarizedFractalEfficiency': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
