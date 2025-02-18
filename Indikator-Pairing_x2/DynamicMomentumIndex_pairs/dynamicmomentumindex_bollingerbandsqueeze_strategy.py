import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
