import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
