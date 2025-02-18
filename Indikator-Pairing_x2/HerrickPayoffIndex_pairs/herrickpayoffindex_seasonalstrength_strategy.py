import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
