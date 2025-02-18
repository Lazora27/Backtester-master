import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'CCITurbo': 1.0
        })
    )
