import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
