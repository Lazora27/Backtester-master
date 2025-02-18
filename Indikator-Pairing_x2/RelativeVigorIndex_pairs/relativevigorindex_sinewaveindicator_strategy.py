import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
