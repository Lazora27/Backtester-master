import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
