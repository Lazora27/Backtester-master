import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
