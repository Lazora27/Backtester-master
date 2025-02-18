import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
