import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
