import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
