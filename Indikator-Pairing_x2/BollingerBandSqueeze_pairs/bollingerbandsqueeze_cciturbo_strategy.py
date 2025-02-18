import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'CCITurbo': 1.0
        })
    )
