import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und MassIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'MassIndex': 1.0
        })
    )
