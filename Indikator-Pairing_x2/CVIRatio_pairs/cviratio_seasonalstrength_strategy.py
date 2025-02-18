import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SeasonalStrength': 1.0
        })
    )
