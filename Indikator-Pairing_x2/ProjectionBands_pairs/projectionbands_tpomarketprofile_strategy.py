import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
