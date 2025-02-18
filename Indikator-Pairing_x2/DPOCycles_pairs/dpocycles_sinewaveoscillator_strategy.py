import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
