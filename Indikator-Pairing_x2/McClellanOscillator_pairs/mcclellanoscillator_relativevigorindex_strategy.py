import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
