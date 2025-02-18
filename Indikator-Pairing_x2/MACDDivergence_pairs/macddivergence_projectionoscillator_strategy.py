import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
