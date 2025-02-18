import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'WeightedCycle': 1.0
        })
    )
