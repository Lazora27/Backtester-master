import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'TimeCycle': 1.0
        })
    )
