import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
