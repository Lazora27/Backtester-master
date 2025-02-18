import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
