import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
