import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
