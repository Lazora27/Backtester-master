import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und CCITurbo
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'CCITurbo': 1.0
        })
    )
