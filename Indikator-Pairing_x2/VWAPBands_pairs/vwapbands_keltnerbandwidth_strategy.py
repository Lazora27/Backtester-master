import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
