import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
