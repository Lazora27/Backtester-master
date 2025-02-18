import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'StochasticOscillator': 1.0
        })
    )
