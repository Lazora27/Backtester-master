import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'McClellanOscillator': 1.0
        })
    )
