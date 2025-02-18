import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FisherTransform
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FisherTransform': 1.0
        })
    )
