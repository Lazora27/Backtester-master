import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
