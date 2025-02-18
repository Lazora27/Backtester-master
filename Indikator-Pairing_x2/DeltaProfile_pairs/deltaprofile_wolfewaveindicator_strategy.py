import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
