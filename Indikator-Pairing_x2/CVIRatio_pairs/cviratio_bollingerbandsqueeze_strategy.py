import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
