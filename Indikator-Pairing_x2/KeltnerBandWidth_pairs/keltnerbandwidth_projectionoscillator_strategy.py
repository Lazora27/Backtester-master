import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
