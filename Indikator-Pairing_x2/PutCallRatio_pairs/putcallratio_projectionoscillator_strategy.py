import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
