import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
