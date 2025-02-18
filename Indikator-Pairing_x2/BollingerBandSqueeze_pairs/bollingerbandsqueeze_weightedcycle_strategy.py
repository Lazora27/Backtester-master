import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'WeightedCycle': 1.0
        })
    )
