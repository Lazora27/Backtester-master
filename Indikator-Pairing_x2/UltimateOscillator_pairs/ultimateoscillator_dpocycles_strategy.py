import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
