import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
