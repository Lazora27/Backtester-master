import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
