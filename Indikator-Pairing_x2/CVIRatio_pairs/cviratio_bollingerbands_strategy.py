import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BollingerBands
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BollingerBands': 1.0
        })
    )
